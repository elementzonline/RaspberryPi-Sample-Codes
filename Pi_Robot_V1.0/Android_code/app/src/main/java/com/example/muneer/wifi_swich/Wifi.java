package com.example.muneer.wifi_swich;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.os.Handler;
import android.widget.TextView;
import android.widget.ToggleButton;

public class Wifi extends Activity {
    Socket s;
    DataInputStream i;
    public  String data;
    public int flag8;
    public String password="";
    InetAddress in;
    String password1;
    PrintWriter out;
    Thread workerThread;
    boolean stopWorker;
    Context context;
    ToggleButton s1,s2;
    TextView t1;
    static int flag1;
    Handler h = new Handler();

    public Wifi(Context c,ToggleButton b,ToggleButton b1,TextView t){
        context = c;
        s1 = b;
        s2 = b1;
        t1=t;
    }
    class CT implements Runnable{
        String ip1;
        int port1;
        public CT(String ip,int port){
            ip1=ip;
            port1=port;
        }
        @Override
        public void run(){
            try{
                in = InetAddress.getByName(ip1);
                s = new Socket(in,port1);
                i = new DataInputStream(s.getInputStream());
                send("query");
                receive();
            }catch(Exception e){}
        }
    }
    public void send(String str){
        try{
            out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(s.getOutputStream())),true);
            out.println(str);
            receive();
        }catch(Exception e){}
    }
    public void receive(){
        stopWorker=false;
        workerThread = new Thread(new Runnable() {
            public void run() {
                while(!Thread.currentThread().isInterrupted()&&!stopWorker)
                {
                    try{
                        int n = i.available();
                        if(n>0){
                            byte[] received = new byte[n];
                            i.read(received);
                            data = new String(received,"US-ASCII");
                            h.post(new Runnable()
                            {
                                public void run()
                                {
                                    try{
                                        toggleUi(data);
                                    }
                                    catch(Exception x){}
                                }
                            });
                        }
                    }catch(Exception e){
                        stopWorker=true;
                    }
                }
            }
        });
        workerThread.start();
    }

    public void toggleUi(String data) {
//        flag1=1;
//        s1.setEnabled(true);
//        s2.setEnabled(true);
//        Drawable newPhoneImage;
        if(data.contains("PIROK")){


            t1.setText("PIR IS ON");

        }
        if(data.contains("PIROF")){

            t1.setText("PIR IS OFF");

        }
        if (data.contains("1On"))
            s1.setChecked(true);
        else if(data.contains("1Of"))
            s1.setChecked(false);
        if(data.contains("2On"))
            s2.setChecked(true);
        else if(data.contains("2Of"))
            s2.setChecked(false);
    }

    class Close implements Runnable{

        @Override
        public void run() {
            // TODO Auto-generated method stub
            try{
                i.close();
                out.close();
                s.close();
            }
            catch(Exception e){}
        }

    }
}