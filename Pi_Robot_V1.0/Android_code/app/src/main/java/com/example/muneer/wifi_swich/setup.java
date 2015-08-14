package com.example.muneer.wifi_swich;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

/**
 * Created by muneer on 01-Aug-15.
 */
public class setup extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.setup);
        Button connect=(Button) findViewById(R.id.button5);
        connect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                EditText ipaddress =(EditText)findViewById(R.id.editText3);
                EditText portnumber =(EditText)findViewById(R.id.editText4);
                String str = ipaddress.getText().toString();
                String a=portnumber.getText().toString();
                if (a.matches("")) {
                    Toast.makeText(getApplication(),"PORT number is empty",Toast.LENGTH_SHORT).show();
                    return;
                }
               else { Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                intent.putExtra("SERVERPORT",a);
                intent.putExtra("SERVER_IP",str);
                startActivity(intent);}
            }
        });

    }
}
