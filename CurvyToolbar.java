package com.example.pachack;


import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Typeface;
import android.util.AttributeSet;

public class CurvyToolbar extends androidx.appcompat.widget.AppCompatTextView {
    private Path path;
    private String text;
    private Paint paint;

    public CurvyToolbar(Context context) {
        super(context);
        init();
    }

    public CurvyToolbar(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public CurvyToolbar(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init();
    }

    private void init() {
        Path p = new Path();
        p.moveTo(0,0);
        p.cubicTo(100,50,200,150,300,200);
        p.lineTo(300,0);
        p.close();

        Paint paint = new Paint();
        paint.setColor(Color.WHITE);
        paint.setStyle(Paint.Style.FILL);
        paint.setTextSize(24);
        paint.setTypeface(Typeface.DEFAULT_BOLD);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        // Draw the curvy shape here
        canvas.drawTextOnPath(text, path, 0, 0, paint);
    }

    @Override
    protected void onTextChanged(CharSequence text, int start, int lengthBefore, int lengthAfter) {
        super.onTextChanged(text, start, lengthBefore, lengthAfter);
        this.text = text.toString();
    }
}
