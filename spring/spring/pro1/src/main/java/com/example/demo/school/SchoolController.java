package com.example.demo.school;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class SchoolController {

    private final SchoolService schoolservice;

    public SchoolController(SchoolService schoolservice) {
        this.schoolservice = schoolservice;
    }
    @PostMapping("/schools")
    private SchoolDto create(@RequestBody SchoolDto dto){
        return this.schoolservice.create(dto);
    }

    @GetMapping("/schools")
    private List<SchoolDto> findAll(){
        return this.schoolservice.findAll();
    }
}
