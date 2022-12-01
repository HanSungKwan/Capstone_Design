// ignore_for_file: prefer_const_literals_to_create_immutables

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'UserInput.dart';
import 'LoginBtn.dart';

class MyLoginPage extends StatefulWidget {
  // const MyLoginPage({Key? key}) : super(key: key);
  const MyLoginPage({super.key, required this.title});
  final String title;

  @override
  State<MyLoginPage> createState() => _MyLoginPageState();
}


class _MyLoginPageState extends State<MyLoginPage> {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Login UI',
        theme: ThemeData(
          primarySwatch: Colors.green,
        ),
        home: Scaffold(
          body: Container(
              alignment: Alignment.center,
              child: makeBody()
          ),
        )
    );
  }
}

Widget makeBody() {

  // // svg 배경이미지 준비
  // final String assetName = 'imgs/login_bg.svg';
  // final Widget loginBgImage = SvgPicture.asset(
  //   assetName,
  //   width: double.infinity, // 가로 최대
  //   height: 300,
  // );

  return ListView(
    children: [
      Column(
        children: [
          // loginBgImage,
          // Padding(
          //   padding: const EdgeInsets.only(bottom: 0, left: 30, right: 30, top: 38),
          //   child: LoginTitleSection(),
          // ),
          Padding(
              padding: const EdgeInsets.only(bottom: 68, left: 30, right: 30, top: 40),
              child: Column(
                children: [
                  // 이메일 입력
                  UserInput(hint: "이메일"),
                  SizedBox(height: 38),
                  UserInput(hint: "비밀번호", isSecure: true),
                  SizedBox(height: 20),
                  Row(
                    children: [
                      Spacer(),
                      Text(
                        '비밀번호를 잊으셨나요?',
                        style: TextStyle(
                          color: Color.fromRGBO(108, 127, 144, 1),
                          fontSize: 14,
                          fontWeight: FontWeight.w400, // regular
                        ),
                      ),
                    ],
                  )
                ],
              )
          ),
          Text(
              '회원 가입하러 가기',
              style: TextStyle(
                color: Color.fromRGBO(108, 127, 144, 1),
                fontSize: 14,
                fontWeight: FontWeight.w400, // regular
              )
          ),
          SizedBox(height: 20),
          Padding(
            padding: const EdgeInsets.only(bottom: 40, left: 30, right: 30),
            child: LoginBtn(),
          ),
        ],
      ),
    ],
  );
}