import 'dart:async';

import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:socket_io_client/socket_io_client.dart' as IO;

class ChatController extends GetxController {
  late IO.Socket socket;
  DateTime now = DateTime.now();
  //establishing connection statuses and receiving restaraunt messages
  String? status;

  socketConnection() {
    socket.onConnect((data) {
      if (data != null) {}
      socket.emit("connection", {
        'username': 'anonymous',
      });
      status = "You Connected.";

      update();
    });
    socket.onDisconnect((data) {
      status = "Server is Down.";
      update();
    });
    /*socket.onConnectError((data) {
      //print(data);
      status = "Connection Error";

      update();
    });*/
    socket.on('message', (data) {
      //DateTime now = DateTime.now();

      if (data['feedback'] == "Sent-Status") {
        print(data);
      } else {
        chat.add({
          "message": data['message'],
          "id": 2,
          'datetime': "${now.hour}:${now.minute}",
          'status': true
        });

        chatExperience();
      }

      update();
    });
  }

  final ScrollController controller = ScrollController();
  //scroll the listview to the very bottom everytime the user inputs a message
  chatExperience() {
    Timer(const Duration(milliseconds: 100), () {
      controller.animateTo(
        controller.position.maxScrollExtent,
        //scroll the listview to the very bottom everytime the user inputs a message
        curve: Curves.easeInOutCubic,
        duration: const Duration(milliseconds: 300),
      );
    });
  }

  //sending a message to restaraunt client
  sendMessage(msg) {
    socket.emit('message', {'message': msg, 'username': 'anonymous'});

    update();
  }

//adds sender message to chat list
  addSenderMessage(msg) {
    //get current datetime only hour and minutes

    DateTime now = DateTime.now();

    chat.add(
      {
        'message': msg,
        'id': 1,
        'datetime': "${now.hour}:${now.minute}",
        'status': true
      },
    );
    update();
  }

  List chat = [];

  List hotWords = [
    "Why a chatbot",
    "Predict for 2 years",
    "commands",
    "Data columns",
    "Hello",
    "Data shape",
  ];
}
