  (function() {

    function setupItemForm(id, method, verb) {
      var form = document.getElementById(id);
      var errorMessage = 'There was an error ' + 
        method === 'POST' ? 'creating' : 'updating' + 
        ' your item';
      var successMessage = 'Item successfully ' + 
        method === 'POST' ? 'created' : 'updated';
      
      form.addEventListener('submit', function(e) {
        var formData = new FormData(e.target);
        var formAction = form.getAttribute('action');

        fetch(formAction, {
          method: method,
          body: formData,
          credentials: 'same-origin',
        })
          .then(function(response){
            if (response.ok && response.redirected) {
              alert(successMessage);
              window.location.href = response.url
            } else {
              // just makes sure to cascade to catch
              throw new Error('general error');
            }
          })
          .catch(function() {
            alert(errorMessage);
          })
        e.preventDefault();
      });
    }

    function setupDeleteButton(id, name) {
      document.getElementById('delete-button')
        .addEventListener('click', function(){
          if (confirm('Are you sure you want to delete "' + name + '"?')) {
            fetch('/item/delete/' + id, {
              method: 'DELETE',
            })
              .then(function(response){
                if (response.ok && response.redirected) {
                  alert(name + ' successfully deleted');
                  window.location.href = response.url
                } else {
                  // just makes sure to cascade to catch
                  throw new Error('general error');
                }
              })
              .catch(function(e) {
                alert('There was an error deleting "' + name + '"')
              })
          }
        });
    }

    function getSignInCallback(state) {
      console.log('getting signInCallback', state)
      return function signInCallback(authResult) {
        if (authResult['code']) {
          // Hide the sign-in button now that the user is authorized
          document.getElementById('signInButton').setAttribute('style', 'display: none');
          // Send the one-time-use code to the server, if the server responds, write a 'login successful' message to the web page and then redirect back to the main restaurants page
          fetch('/gconnect?state=' + state, {
            method: 'POST',
            body: authResult['code'],
            credentials: 'same-origin',
            headers: new Headers({
              'Content-Type': 'application/octet-stream; charset=utf-8',
            })
          })
          .then(function(result) {
            return result.text();
          })
          .then(function(result) {
            // Handle or verify the server response if necessary.
            if (result) {
              document.getElementById('result').innerHTML = 'Login Successful!</br>'+ result + '</br>Redirecting...';
              setTimeout(function() {
                window.location.href = "/";
              }, 4000);
              
            } else if (authResult['error']) {
              console.log('There was an error: ' + authResult['error']);
            } else {
              $('#result').html('Failed to make a server-side call. Check your configuration and console.');
            }
          })
        }
      }
    }

    window.itemCatalog = {
      setupItemForm: setupItemForm,
      setupDeleteButton: setupDeleteButton,
      getSignInCallback: getSignInCallback
    };
  })()
  