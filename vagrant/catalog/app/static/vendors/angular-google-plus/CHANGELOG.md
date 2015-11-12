## 0.1.2

- Bower: remove minifed version from main value
- Dependencies: remove connect dependency (Gruntfile)
- API: Add the getUser method and remove it from login (#1, #4)

#### Breaking Changes

The API for login has been changed (#4):

**Before:**

```javascript
GooglePlus.login().then(function (user) {
    console.log(user);
}, function (err) {
    console.log(err);
});
```

**After:**

```javascript
GooglePlus.login().then(function (authResult) {
    console.log(authResult);

    GooglePlus.getUser().then(function (user) {
        console.log(user);
    });
}, function (err) {
    console.log(err);
});
```

## 0.1.1

- added setToken / getToken methods

## 0.1.0

- Initial release