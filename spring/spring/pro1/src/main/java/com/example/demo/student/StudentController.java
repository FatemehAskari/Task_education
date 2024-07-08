package com.example.demo.student;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;

@RestController
public class StudentController {
    private final StudentService studentservice;
    public StudentController(StudentService studentservice) {
        this.studentservice = studentservice;
    }

    @PostMapping("/students")
    public StudentResponseDto saveStudent(
         @Valid @RequestBody StudentDto dto
    ){
        return this.studentservice.savestudent(dto);
    }
    @GetMapping("/students/{student-id}")
    public StudentResponseDto findStudent(
            @PathVariable("student-id") Integer id
    ){
        return this.studentservice.findStudent(id);
    }

    @GetMapping("/students")
    public List<StudentResponseDto>  findAllStudent(
    ){
        return this.studentservice.findallstudent();
    }

    @GetMapping("/students/search/{student-name}")
    public List<StudentResponseDto> findstudentbyname(
            @PathVariable("student-name") String firstname
    ){
        return this.studentservice.findstudentbyname(firstname);
    }

    @DeleteMapping("/students/{student-id}")
    @ResponseStatus(HttpStatus.OK)
    public void deletestudent(
            @PathVariable("student-id") Integer id
    ){
         this.studentservice.deletestudent(id);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<?> handleMethodArgumentNotValidException(
          MethodArgumentNotValidException exp
    ){
        var errors=new HashMap<String,String>();
        exp.getBindingResult().getAllErrors()
                .forEach(error->{
                    var fieldName=((FieldError)error).getField();
                    var errorMessage=error.getDefaultMessage();
                    errors.put(fieldName,errorMessage);
                });
        return new ResponseEntity<>(errors,HttpStatus.BAD_REQUEST);
    }

}
