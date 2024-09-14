package com.example.pachack;

public class SentenceRequest {
    private String sentence;

    public SentenceRequest(String sentence) {
        this.sentence = sentence;
    }

    public String getSentence() {
        return sentence;
    }

    public void setSentence(String sentence) {
        this.sentence = sentence;
    }
}
