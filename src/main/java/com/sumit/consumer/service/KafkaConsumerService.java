package com.sumit.consumer.service;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumerService {

    private final SimpMessagingTemplate messagingTemplate;

    public KafkaConsumerService(SimpMessagingTemplate messagingTemplate) {
        this.messagingTemplate = messagingTemplate;
    }

    @KafkaListener(topics = "tic-data-topic", groupId = "group_id")
    public void consume(String message) {
        System.out.println("Received message from Kafka: " + message);
        messagingTemplate.convertAndSend("/topic/tic-data", message);
    }
}