import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:crypto/crypto.dart';
import 'package:my_first_project/database/memo.dart';
import 'package:my_first_project/database/db.dart';
import 'package:my_first_project/screens/view.dart';
import 'edit.dart';

// class MyHomePage extends StatefulWidget {
//   const MyHomePage({super.key, required this.title});
//   final String title;
//
//   @override
//   State<MyHomePage> createState() => _MyHomePageState();
// }
class MainPage extends StatefulWidget{
  HomePage createState()=> HomePage();
}

class HomePage extends State<MainPage> {
  String deleteId = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("내 프로젝트"),
      ),
      body: Column(
        children: <Widget>[
          Padding(
            padding: EdgeInsets.only(left: 20, top: 20, bottom: 20),
             // child: Text('프프젝젝',
             //     style: TextStyle(fontSize: 30, color: Colors.yellow))
          ),
          Expanded(child: memoBuilder(context))
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          Navigator.push(
              context, CupertinoPageRoute(builder: (context) => EditPage()));
        },
        tooltip: '새프로젝트를 추가하려면 클릭',
        label: Text('추가'),
        icon: Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }

  Future<List<Memo>> loadMemo() async {
    DBHelper sd = DBHelper();
    return await sd.memos();
  }

  Future<void> deleteMemo(String id) async {
    DBHelper sd = DBHelper();
    await sd.deleteMemo(id); // sd에서 가져온거, 위 deleteMemo와 다름
  }

  void showAlertDialog(BuildContext context) async {
    String result = await showDialog(
      context: context,
      barrierDismissible: false, // user must tap button!
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('삭제'),
          content: Text("정말 삭제하시겠습니까?"),
          actions: <Widget>[
            TextButton(
              child: Text('Delete'),
              onPressed: () {
                Navigator.pop(context, "Delete");
                setState(() {
                  deleteMemo(deleteId);
                });
                deleteId = '';
              },
            ),
            TextButton(
              child: Text('Cancel'),
              onPressed: () {
                deleteId = '';
                Navigator.pop(context, "Cancel");
              },
            ),
          ],
        );
      },
    );
  }

  Widget memoBuilder(BuildContext parentContext) {
    return FutureBuilder(
      builder: (context, Snap) {
        if ((Snap.data as List).length == 0) {
          return Container(
            alignment: Alignment.center,
            child: Text("프로젝트를 추가해주세요.\n\n\n\n",
              style: TextStyle(fontSize: 15, color: Colors.black54),
            ),);
        }

        return ListView.builder(
          physics: BouncingScrollPhysics(),
          padding: EdgeInsets.all(20),
          itemCount: (Snap.data as List).length,
          itemBuilder: (context, index) {
            Memo memo = (Snap.data as List)[index];
            return InkWell(
              onTap: (){},
                //Navigator.push(
                //    parentContext, CupertinoPageRoute(builder: (context) => ViewPage(id: memo.id)));

              onLongPress: (){
                deleteId = memo.id;
                showAlertDialog(parentContext);
              },
              child: Container(
                margin: EdgeInsets.all(5),
                padding: EdgeInsets.all(15),
                alignment: Alignment.center,
                height: 100,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: <Widget>[
                    Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: <Widget>[
                        Text(memo.title,
                            style: TextStyle(
                                fontSize: 20, fontWeight: FontWeight.w500)),
                        Text(memo.text, style: TextStyle(fontSize: 15)),
                      ],
                    ),
                    Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: <Widget>[
                        Text("프로젝트 생성 시간: " + memo.createTime.split('.')[0],// ms까지 나와서 split
                          style: TextStyle(fontSize: 11),
                          textAlign: TextAlign.end,
                        ),
                      ],
                    )
                  ],
                ),
                decoration: BoxDecoration(
                  // color: Color.fromRGBO(201, 237, 188, 1), // 박스 안 색상 상세히 변경 시
                  color: Colors.white,
                  border: Border.all(
                    color: Colors.green,
                    width: 2,
                  ),
                  boxShadow: [BoxShadow(color: Colors.lightGreen, blurRadius: 2)],
                  borderRadius: BorderRadius.circular(12),
                )),
            );
          },
        );
      },
      future: loadMemo(),
    );
  }
}
