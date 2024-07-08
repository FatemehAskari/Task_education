package com.example.demo.school;

import com.example.demo.school.SchoolDto;
import com.example.demo.school.SchoolMapper;
import com.example.demo.school.SchoolRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class SchoolService {
    private final SchoolMapper schoolmapper;
    private final SchoolRepository schoolrepository;

    public SchoolService(SchoolMapper schoolmapper, SchoolRepository schoolrepository) {
        this.schoolmapper = schoolmapper;
        this.schoolrepository = schoolrepository;
    }

    public SchoolDto create(SchoolDto dto){
        var school=schoolmapper.covertdtotoschool(dto);
        schoolrepository.save(school);
        return dto;
    }

    public List<SchoolDto> findAll(){
        return schoolrepository.findAll()
                .stream()
                .map(schoolmapper::toSchoolDto)
                .collect(Collectors.toList());
    }
}
