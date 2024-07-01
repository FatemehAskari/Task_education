package com.example.demo.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

import static java.util.Calendar.JANUARY;

@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(
            StudentRepository repository){
        return args -> {
            Student mariam=new Student(
                    "Mariam",
                    23,
                    LocalDate.of(2000, Month.JANUARY,5),
                    "maryam.jamal@gmail.com"
            );

            Student alex=new Student(
                    "alex",
                    21,
                    LocalDate.of(2004, Month.JANUARY,5),
                    "alex@gmail.com"
            );

            repository.saveAll(
                    List.of(mariam,alex)
            );
        };
    }
}
