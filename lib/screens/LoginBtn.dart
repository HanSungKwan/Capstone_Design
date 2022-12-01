import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'home.dart';

class LoginBtn extends StatelessWidget {

  @override
  Widget build(BuildContext context) {

    return SizedBox(
      height: 50.0,
      child: Container(
        decoration: BoxDecoration(
            //color: Color.fromRGBO(48, 58, 82, 1),
            color: Colors.green,
            borderRadius: BorderRadius.all(Radius.circular(20.0))
        ),
        child: Stack(
          children: [
            Row(
              children: [
                Expanded(
                  child: Center(
                    child: Text(
                      '로그인',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 14,
                        fontWeight: FontWeight.w600, // bold
                      ),
                    ),
                  ),
                )
              ],
            ),
            SizedBox.expand(
              child: Material(
                type: MaterialType.transparency,
                child: InkWell(onTap: (){
                          Navigator.push(
                          context, CupertinoPageRoute(builder: (context) => MainPage()));
                          print('로그인 버튼 클릭');
                }),
              ),
            )
          ],
        ),
      ),
    );
  }
}