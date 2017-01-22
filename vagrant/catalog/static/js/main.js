/**
 * Callback for successful Google Sign-in
 * @param googleUser The google user object
 */
function onSignIn(googleUser) {
    // Useful data for your client-side scripts:
    var profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Don't send this directly to your server!
    console.log('Full Name: ' + profile.getName());
    console.log('Given Name: ' + profile.getGivenName());
    console.log('Family Name: ' + profile.getFamilyName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());

    // The ID token you need to pass to your backend:
    var id_token = googleUser.getAuthResponse().id_token;
    console.log("ID Token: " + id_token);

    $.ajax({
        url: '/gsignin?state={{ state }}',
        type: 'POST',
        data: {'id': id_token,
            'email': profile.getEmail(),
            'image_url': profile.getImageUrl()}
    }).done(function () {
        setTimeout(function () {
            window.location.href = '/categories';
        }, 2000);
    });
}

// function signOut() {
//     var auth2 = gapi.auth2.getAuthInstance();
//     auth2.signOut().then(function () {
//         console.log('User signed out.')
//         setTimeout(function () {
//             window.location.href = '/';
//         }, 1000);
//     })
// }
