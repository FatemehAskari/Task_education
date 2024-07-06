package com.example.demo;

public record OrderRecord(
        String customerName,
        String productName,
        int quantity
) {
}
