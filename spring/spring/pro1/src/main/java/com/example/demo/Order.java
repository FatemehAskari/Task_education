package com.example.demo;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

public class Order {

    @JsonProperty("c-name")
    private String customerName;

    @JsonProperty("p-name")
    private String productName;

    @JsonProperty("q-name")
    private int quantity;

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return "Order{" +
                "customerName='" + customerName + '\'' +
                ", productName='" + productName + '\'' +
                ", quantity=" + quantity +
                '}';
    }
}
