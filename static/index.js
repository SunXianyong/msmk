
$(document).ready(function () {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + '/dcenter');
    socket.on('connect', function () {
        socket.send("客户端已连接")
    });

    $('form#joinRoom').submit(function (event) {
        socket.emit('joinRoom', {
            room: $('#roomNum').val()
        });
        return false
    });

    socket.on("roomJoined", function (msg, cb) {
        $('#chatContent').append('<li>' + msg.user + '已加入房间' + msg.room + '</li>')
    });

    socket.on("roomLeft", function (msg, cb) {
        $('#chatContent').append('<li>' + msg.user + '已退出房间' + msg.room + '</li>')
    });

    socket.on("roomLeftPersonal", function (msg, cb) {
        $('#chatContent').append('<li>' + '您已退出房间' + msg.room + '</li>')
    });

    $('#leave_room').on('click', function () {
        socket.emit('leaveRoom', {
            room: $('#roomNum').val()
        });
    });

    $('form#SubmitForm').submit(function () {
        socket.emit('sendMsg', {
            msg: $('#chatMsg').val(),
            room: $('#roomNum').val()
        });
        $('#chatMsg').val("");
        console.log("已发送 " + $('#chatMsg').val())
        return false
    });

    socket.on("SendtoAll", function (msg, cb) {
        $('#chatContent').append('<li>' + msg.user + ': ' + msg.msg + '</li>');
    })
})