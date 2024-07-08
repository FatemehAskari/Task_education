package com.example.demo.school;

import com.example.demo.school.SchoolDto;
import org.springframework.stereotype.Service;

@Service
public class SchoolMapper {
    public School covertdtotoschool(SchoolDto dto){
        var school=new School();
        school.setName(dto.name());
        return school;
    }

    public SchoolDto toSchoolDto(School school){
        return new SchoolDto(school.getName());
    }
}
