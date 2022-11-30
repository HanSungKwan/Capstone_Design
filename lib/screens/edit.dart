import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:my_first_project/database/memo.dart';
import 'package:my_first_project/database/db.dart';
import 'package:crypto/crypto.dart';
import 'dart:convert';

class EditPage extends StatelessWidget {
  String title = '';
  String text = '';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: <Widget>[
          IconButton(
            icon: const Icon(Icons.delete),
            onPressed: (){},
          ),
          IconButton(
            icon: const Icon(Icons.save),
            onPressed: saveDB,
          )
        ],
      ),
      body:Padding(
        padding: EdgeInsets.all(20),
        child: Column(
        children: <Widget>[
          TextField(
            onChanged: (String title){this.title = title;}, //제목 바뀔 때마다 함수 실행-> 변경사항 title에 저장
            // style: TextStyle(fontSize: 20, fontWeight: FontWeight.w500),
            keyboardType: TextInputType.multiline,
            maxLines: 2,
            //obscureText: true, 암호화됨
            decoration: InputDecoration(
              //border: OutlineInputBorder(), textfield 박스 유무
              hintText: '제목을 적어주세요.',
            ),
          ),
          Padding(padding: EdgeInsets.all(10)), // textfield 사이 간격
          TextField(
            onChanged: (String text){this.text = text;},
            //obscureText: true, 암호화됨
            decoration: InputDecoration(
              //border: OutlineInputBorder(), textfield박스 유무
              hintText: '아무거나 적어라 임마들아.',
            ),
          ),
        ],
      ),
    ));
  }

  Future<void> saveDB() async {

    DBHelper sd = DBHelper();

    var fido = Memo(
      id: Str2Sha512(DateTime.now().toString()),
      title: this.title,
      text: this.text,
      createTime: DateTime.now().toString(),
      editTime: DateTime.now().toString(),
    );
    await sd.insertMemo(fido);

    print(await sd.memos());
  }
}
  String Str2Sha512(String text) {
    var bytes = utf8.encode("text"); // data being hashed
    var digest = sha512.convert(bytes);
    return digest.toString();
  }
