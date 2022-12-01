import 'package:flutter/material.dart';

// 사용자 입력 부분
class UserInput extends StatelessWidget {

  String hint;
  double width, height;
  bool isSecure;

  // {} 를 하면 매개변수에 기본값을 넣을 수 있다.
  // 생성자 메소드
  UserInput({String hint = "힌트 없음",
    double width = 100.0,
    double height = 100.0,
    bool isSecure = false
  }) :
        hint = hint,
        width = width,
        height = height,
        isSecure = isSecure;

  @override
  Widget build(BuildContext context) {

    // 포커스 여부
    FocusNode myFocusNode = new FocusNode();

    Color focusColor = Color.fromRGBO(108, 127, 144, 1);
    Color normalColor = Color.fromRGBO(108, 127, 144, 1);


    return TextField(
      obscureText: isSecure, // 비밀번호 여부
      style: TextStyle(color: normalColor),
      decoration: InputDecoration(
          border: OutlineInputBorder(),
          labelText: this.hint, // placeholder
          labelStyle: TextStyle(
              color: myFocusNode.hasFocus ? focusColor : normalColor
          ),
          focusColor: focusColor,
          focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(color: focusColor, width: 3.0),
          )
      ),
    );
  }
}