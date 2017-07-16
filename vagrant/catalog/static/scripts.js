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
      alert('setting up');
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

    window.itemCatalog = {
      setupItemForm: setupItemForm,
      setupDeleteButton: setupDeleteButton,
    };
  })()
  