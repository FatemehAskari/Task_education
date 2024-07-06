package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		var ctx=SpringApplication.run(DemoApplication.class, args);
		MyFirstService myfirsevice = ctx.getBean(MyFirstService.class);

		System.out.println(myfirsevice.tellAStory());
//		System.out.println(myfirsevice.getJavaVersion());
//		System.out.println(myfirsevice.getOSName());
//		System.out.println(myfirsevice.readProp());
	}

}
