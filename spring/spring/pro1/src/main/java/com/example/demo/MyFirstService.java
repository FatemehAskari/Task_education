package com.example.demo;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Service;

@Service
public class MyFirstService {


    private final  MyFirstClass myfirstclass;

    public MyFirstService(
          @Qualifier("mysecondclass")  MyFirstClass myfirstclass) {
        this.myfirstclass = myfirstclass;
    }

    public String tellAStory(){
        return "the dependency is saying : " +myfirstclass.sayHello();
    }
}
