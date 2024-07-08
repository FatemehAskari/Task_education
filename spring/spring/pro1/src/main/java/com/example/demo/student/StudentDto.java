package com.example.demo.student;

import jakarta.persistence.Column;
import jakarta.validation.constraints.NotEmpty;

public record StudentDto(
     @NotEmpty(message = "Firstname should not be empty")
     String firstname,
     @NotEmpty(message="lastname should not be empty")
     String lastname,
     String email,
     Integer schoolId
) {

}
