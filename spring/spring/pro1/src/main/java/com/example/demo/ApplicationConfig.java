package com.example.demo;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

@Configuration
public class ApplicationConfig {

    @Bean
    public MyFirstClass myfirstclass(){
        return new MyFirstClass("First bean");
    }

    @Bean
    public MyFirstClass mysecondclass(){
        return new MyFirstClass("second bean");
    }

    @Bean
//    @Primary
    public MyFirstClass mythirdsclass(){
        return new MyFirstClass("third bean");
    }
}
