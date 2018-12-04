package com.example.akaneyoh.stevtourguidev3;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Main2Activity extends AppCompatActivity {

    String urlPath;
    String startRoom;
    String endRoom;

    EditText startRoomInput;
    EditText endRoomInput;

    Button findRoomButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        startRoomInput = findViewById(R.id.startRoomInput);
        endRoomInput = findViewById(R.id.endRoomInput);

        findRoomButton = findViewById(R.id.findRoomButton);
        findRoomButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startRoom = startRoomInput.getText().toString();
                endRoom = endRoomInput.getText().toString();

                urlPath = "http://18.212.189.150:5000/routeFinder/" + startRoom + "/" + endRoom;
                Uri uri = Uri.parse(urlPath);
                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                startActivity(intent);
            }
        });
    }
}