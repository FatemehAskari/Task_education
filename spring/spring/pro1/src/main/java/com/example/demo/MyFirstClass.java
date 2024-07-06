package com.example.demo;


import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import java.security.Provider;

//@Component
//@Service
public class MyFirstClass {

    private String myVar;

    public MyFirstClass(String myVar) {
        this.myVar = myVar;
    }

    public String sayHello(){
        return "Hello everybody ==> myVar =" + myVar;
    }
}
