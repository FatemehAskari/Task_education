package com.example.demo.student;

import com.example.demo.student.*;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class StudentService {
    private final StudentRepository repository;
    private final StudentMapper studentmapper;

    public StudentService(StudentRepository repository, StudentMapper studentmapper) {
        this.repository = repository;
        this.studentmapper = studentmapper;
    }
    public StudentResponseDto savestudent(
            StudentDto dto
    ){
        var student=studentmapper.toStudent(dto);
        var saveStudent= repository.save(student);
        return studentmapper.toStudentResponseDto(saveStudent);
    }

    public StudentResponseDto findStudent(Integer id){
        return repository.findById(id)
                .map(studentmapper::toStudentResponseDto)
                .orElse(null);
    }
    public List<StudentResponseDto> findallstudent(){
        List<Student> Allstudent;
        Allstudent=repository.findAll();
        List<StudentResponseDto> Allstudentdto=Allstudent.stream()
                .map(studentmapper::toStudentResponseDto)
                .collect(Collectors.toList());
        return Allstudentdto;
    }
    public List<StudentResponseDto> findstudentbyname(String name){
        return repository.findAllByFirstnameContaining(name)
                .stream()
                .map(studentmapper::toStudentResponseDto)
                .collect(Collectors.toList());
    }

    public void deletestudent(Integer id){
        repository.deleteById(id);
    }
}
