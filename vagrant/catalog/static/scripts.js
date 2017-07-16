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

    window.itemCatalog = {
      setupItemForm: setupItemForm,
    };
  })()
  