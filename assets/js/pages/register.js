function button_register() {
    var {PythonShell} = require("python-shell");
    var path = require("path");

    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    let info_data_py = {
        function_name: 'register_user',
        username: username,
        email: email,
        password: password
    };

    // Convert userdata to a JSON string
    let info_data_py_Json = JSON.stringify(info_data_py);

    var scriptPath = path.join(__dirname, './engine');
    console.log('Script Path:', scriptPath); // Debug statement

    var options = {
        scriptPath: scriptPath, // path to your script
        args: [info_data_py_Json] // pass arguments to the python script here
    };

    var register = new PythonShell('register.py', options);

    register.on('message', function(message) {
        console.log('Resultados: ', message);
    });

    register.end(function (err) {
        if (err) throw err;
        console.log('finished');
    });
}