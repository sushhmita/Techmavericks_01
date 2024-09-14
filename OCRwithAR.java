package com.example.pachack;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import androidx.appcompat.app.AppCompatActivity;


public class OCRwithAR extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.ocrwithar);

        WebView webView = findViewById(R.id.webview);

        // Enable JavaScript (if needed)
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);

        // Set a WebViewClient to handle navigation within the WebView
        webView.setWebViewClient(new WebViewClient());

        // Load HTML content
        String htmlContent = "<html><body><h1>Hello, WebView!</h1><p>This is an example of HTML content.</p></body></html>";
        webView.loadData(htmlContent, "demo/html", "UTF-8");

    }


}
