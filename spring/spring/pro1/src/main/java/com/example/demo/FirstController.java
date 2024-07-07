package com.example.demo;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
public class FirstController {

//    @GetMapping("/hello")
//    public String sayHello(){
//        return "Hello from my first controller";
//    }

    private final StudentRepository repository;


    public FirstController(StudentRepository repository) {
        this.repository = repository;
    }

    @PostMapping("/students")
    public Student post(
          @RequestBody Student student
    ){
        return repository.save(student);
    }

    @GetMapping("/students/{student-id}")
    public Student findStudent(
            @PathVariable("student-id") Integer id
    ){
        return repository.findById(id)
                .orElse(new Student());
    }

    @GetMapping("/students")
    public List<Student>  findAllStudent(
    ){
        return repository.findAll();
    }

    @GetMapping("/students/search/{student-name}")
    public List<Student>  findstudentbyname(
            @PathVariable("student-name") String firstname
    ){
        return repository.findAllByFirstnameContaining(firstname);
    }

    @DeleteMapping("/students/{student-id}")
    @ResponseStatus(HttpStatus.OK)
    public void deletestudent(
            @PathVariable("student-id") Integer id
    ){
         repository.deleteById(id);
    }

}
