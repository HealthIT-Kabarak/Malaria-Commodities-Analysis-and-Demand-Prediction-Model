import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:chat_bubbles/bubbles/bubble_special_one.dart';
import 'package:chat_bubbles/chat_bubbles.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:predict/chatcontrollers.dart';
import 'package:socket_io_client/socket_io_client.dart' as IO;

class ChatPage extends StatefulWidget {
  const ChatPage({super.key});

  @override
  State<ChatPage> createState() => _ChatPageState();
}

class _ChatPageState extends State<ChatPage> {
  final _textController = TextEditingController();

  //accessing chatcontroller back-logic

  ChatController chatController = Get.put(ChatController());

  @override
  void initState() {
    super.initState();
    chatController.socket = IO.io(
        'http://localhost:3000/',
        IO.OptionBuilder().setTransports(['websocket']).setQuery(
            {'username': "armsy"}).build());
    chatController.socketConnection();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      // backgroundColor: Colors.black,
      appBar: AppBar(
        bottomOpacity: 0,
        elevation: 0,
        backgroundColor: Colors.black,
        title: Column(
          children: [
            const Text("Malaria Commodity Dispersion Explainer",
                style: TextStyle(color: Colors.white)),
            Align(
              alignment: Alignment.center,
              child: GetBuilder<ChatController>(builder: (context) {
                return Text(chatController.status ?? "Connecting...",
                    style: const TextStyle(fontSize: 7, color: Colors.black));
              }),
            ),
          ],
        ),
        centerTitle: true,
      ),
      body: Stack(
        fit: StackFit.expand,
        children: [
          Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              GetBuilder<ChatController>(builder: (_) {
                return Expanded(
                  child: chatController.chat.isEmpty
                      ? Container(
                          //color: Colors.pink,
                          padding: const EdgeInsets.symmetric(vertical: 8),
                          child: Center(
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Container(
                                  height: 80,
                                  width: 80,
                                  decoration: const BoxDecoration(
                                      color: Colors.amber,
                                      image: DecorationImage(
                                          fit: BoxFit.fitWidth,
                                          image: AssetImage(
                                            "assets/bot.jpeg",
                                          )),
                                      borderRadius: BorderRadius.all(
                                          Radius.circular(20))),
                                ),
                                const SizedBox(
                                  height: 5,
                                ),
                                Container(
                                  height: 150,
                                  width: 240,
                                  decoration: BoxDecoration(
                                      color: Colors.grey.shade200,
                                      borderRadius: const BorderRadius.all(
                                          Radius.circular(10))),
                                  child: Center(
                                    child: SizedBox(
                                      width: 220,
                                      child: AnimatedTextKit(
                                        animatedTexts: [
                                          // "Hi! I'm a chatbot for the child protection management system. I can help you report and track cases, answer basic questions and guide you through the process. Let's work together to keep children safe!"
                                          TyperAnimatedText(
                                              "Hi! I'm a chatbot, still in active development.I can give you a clear picture of trends related to consumption of malaria commodities,dissect the dataset and make limitied prediction.")
                                        ],
                                      ),
                                    ),
                                  ),
                                ),
                                const SizedBox(
                                  height: 20,
                                ),
                                const Text(
                                  'Project for Kabarak Hackathon demo @2023.',
                                  style: TextStyle(
                                      fontSize: 10,
                                      fontStyle: FontStyle.italic),
                                ),
                              ],
                            ),
                          ),
                        )
                      : Column(
                          children: [
                            const Center(
                              child: Text(
                                "These messages will cease to exist on exit!",
                                style: TextStyle(fontSize: 10),
                              ),
                            ),
                            Expanded(
                              child: ListView.builder(
                                  controller: chatController.controller,
                                  itemCount: chatController.chat.length,
                                  itemBuilder: (BuildContext ctx, index) =>
                                      chatController.chat[index]['id'] == 1
                                          ? Row(
                                              mainAxisAlignment:
                                                  MainAxisAlignment.end,
                                              children: [
                                                const SizedBox(
                                                  width: 5,
                                                ),
                                                Row(
                                                  children: [
                                                    const SizedBox(
                                                      width: 5,
                                                    ),
                                                    BubbleSpecialOne(
                                                        text:
                                                            "${chatController.chat[index]['message']}",
                                                        isSender: true,
                                                        color: Colors
                                                            .purple.shade100,
                                                        textStyle:
                                                            const TextStyle(
                                                                fontSize: 15,
                                                                color: Colors
                                                                    .purple,
                                                                fontStyle:
                                                                    FontStyle
                                                                        .italic)),
                                                    Container(
                                                      height: 40,
                                                      width: 40,
                                                      decoration: BoxDecoration(
                                                          image: const DecorationImage(
                                                              image: AssetImage(
                                                                  "assets/avatar1.jpeg")),
                                                          color: Colors
                                                              .grey.shade200,
                                                          borderRadius:
                                                              const BorderRadius
                                                                      .all(
                                                                  Radius
                                                                      .circular(
                                                                          10))),
                                                    ),
                                                  ],
                                                ),
                                              ],
                                            )
                                          : Row(
                                              mainAxisAlignment:
                                                  MainAxisAlignment.start,
                                              children: [
                                                const SizedBox(
                                                  width: 5,
                                                ),
                                                Row(
                                                  children: [
                                                    Container(
                                                      height: 40,
                                                      width: 40,
                                                      decoration: BoxDecoration(
                                                          image: const DecorationImage(
                                                              image: AssetImage(
                                                                  "assets/bot.jpeg")),
                                                          color: Colors
                                                              .grey.shade200,
                                                          borderRadius:
                                                              const BorderRadius
                                                                      .all(
                                                                  Radius
                                                                      .circular(
                                                                          10))),
                                                    ),
                                                    const SizedBox(
                                                      width: 5,
                                                    ),
                                                    SizedBox(
                                                      width: 250,
                                                      child: Card(
                                                        elevation: 0,
                                                        color:
                                                            Colors.transparent,
                                                        child: AnimatedTextKit(
                                                          totalRepeatCount: 1,
                                                          animatedTexts: [
                                                            TypewriterAnimatedText(
                                                                textStyle:
                                                                    const TextStyle(
                                                                        fontSize:
                                                                            15),
                                                                "${chatController.chat[index]['message']}")
                                                          ],
                                                        ),
                                                      ),
                                                    ),
                                                  ],
                                                ),
                                                Text(
                                                    "${chatController.chat[index]['datetime']}",
                                                    style: const TextStyle(
                                                        fontSize: 10,
                                                        fontStyle:
                                                            FontStyle.italic)),
                                              ],
                                            )),
                            ),
                          ],
                        ),
                );
              }),
              Align(
                alignment: Alignment.bottomCenter,
                child: Card(
                  color: Colors.black,
                  margin: EdgeInsets.zero,
                  child: Padding(
                    padding: EdgeInsets.only(
                      right: 8,
                      left: 8,
                      bottom: MediaQuery.of(context).viewInsets.bottom > 0
                          ? 7.5
                          : 14,
                      //top: 2, //no to margin near hot and message input
                    ),
                    child: Stack(
                      children: [
                        Column(
                          children: [
                            SizedBox(
                              // color: Colors.blue,
                              height: 50,
                              child: ListView(
                                scrollDirection: Axis.horizontal,
                                padding: const EdgeInsets.all(10.0),
                                children: chatController.hotWords
                                    .map(
                                      (e) => Wrap(children: [
                                        GestureDetector(
                                          onTap: () {
                                            chatController.chatExperience();
                                            chatController.addSenderMessage(e);

                                            chatController.sendMessage(e);
                                          },
                                          child: Chip(
                                              padding:
                                                  const EdgeInsets.all(8.0),
                                              label: Text(
                                                e,
                                                style: const TextStyle(
                                                    fontSize: 10),
                                              )),
                                        ),
                                        const SizedBox(
                                          width: 2,
                                        )
                                      ]),
                                    )
                                    .toList(),
                              ),
                            ),
                            GetBuilder<ChatController>(builder: (_) {
                              return Text(
                                chatController.status ?? "Linking with khis...",
                                style: const TextStyle(
                                    fontSize: 10, color: Colors.white),
                              );
                            }),
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              crossAxisAlignment: CrossAxisAlignment.end,
                              children: [
                                Expanded(
                                  child: Row(
                                    children: [
                                      Expanded(
                                        child: TextField(
                                          controller: _textController,
                                          minLines: 1,
                                          maxLines: 5,
                                          cursorColor: Colors.black,
                                          decoration: InputDecoration(
                                            isDense: true,
                                            contentPadding:
                                                const EdgeInsets.only(
                                                    right: 16,
                                                    left: 20,
                                                    bottom: 10,
                                                    top: 10),
                                            hintStyle: TextStyle(
                                                fontSize: 14,
                                                color: Colors.grey.shade700),
                                            hintText:
                                                "KHIS analysis explainer.",
                                            border: InputBorder.none,
                                            filled: true,
                                            fillColor: Colors.grey.shade100,
                                            enabledBorder: OutlineInputBorder(
                                              borderRadius:
                                                  BorderRadius.circular(20),
                                              gapPadding: 0,
                                              borderSide: BorderSide(
                                                  color: Colors.grey.shade200),
                                            ),
                                            focusedBorder: OutlineInputBorder(
                                              borderRadius:
                                                  BorderRadius.circular(20),
                                              gapPadding: 0,
                                              borderSide: BorderSide(
                                                  color: Colors.grey.shade300),
                                            ),
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                                IconButton(
                                  splashRadius: 20,
                                  icon: const Icon(
                                    Icons.send,
                                    color: Colors.blue,
                                  ),
                                  onPressed: () {
                                    if (_textController.text.isNotEmpty) {
                                      chatController.chatExperience();

                                      chatController
                                          .sendMessage(_textController.text);
                                      chatController.addSenderMessage(
                                          _textController.text);
                                      /*chatController
                                          .sendMessage(_textController.text);*/
                                      _textController.clear();
                                    }
                                  },
                                ),
                              ],
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
