package com.example.pachack;

import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

public class WordClassification extends AppCompatActivity {

    private ApiService apiService;
    private TextView textView;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.wordclassification);

        // Initialize Retrofit
        Retrofit retrofit = RetrofitClient.getClient();
        apiService = retrofit.create(ApiService.class);

        // Initialize TextView
        textView = findViewById(R.id.textView);

        // Example sentence
        String sentence = "Example sentence";

        // Make the network request
        highlightSentence(sentence);
    }

    private void highlightSentence(String sentence) {
        SentenceRequest request = new SentenceRequest(sentence);
        Call<SentencesResponse> call = apiService.highlightSentence(request);

        call.enqueue(new Callback<SentencesResponse>() {
            @Override
            public void onResponse(Call<SentencesResponse> call, Response<SentencesResponse> response) {
                if (response.isSuccessful()) {
                    // Handle the response
                    SentencesResponse sentencesResponse = response.body();
                    if (sentencesResponse != null) {
                        String highlightedSentence = sentencesResponse.getHighlighted_sentence();
                        // Update UI with the highlighted sentence
                        textView.setText(highlightedSentence);
                    }
                } else {
                    Toast.makeText(WordClassification.this, "Error: " + response.code(), Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<SentencesResponse> call, Throwable t) {
                Toast.makeText(WordClassification.this, "Failed to connect: " + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}
