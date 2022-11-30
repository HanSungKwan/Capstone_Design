import 'package:flutter/material.dart';
import 'package:my_first_project/screens/login.dart';
import 'screens/login.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My Project',
      theme: ThemeData(
        primarySwatch: Colors.green, primaryColor: Colors.white,
      ),
      home: const MyLoginPage(title: '내 프로젝트'),
    );
  }
}


