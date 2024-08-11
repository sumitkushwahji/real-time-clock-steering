package com.sumit.consumer.controller;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TicDataController {

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;

    @PostMapping("/publish")
    public void sendDataToKafka(@RequestBody String data) {
        kafkaTemplate.send("tic-data-topic", data);
    }
}
