#include <WiFi.h>
#include <WebServer.h>
#include <FastLED.h>
#include <Arduino.h>

#define LED_PIN 13
#define NUM_LEDS 200 // Change this to match the number of LEDs in your strip

CRGB leds[NUM_LEDS];

const char *ssid = "SHAW-B503";
const char *password = "bright0737cover";

WebServer server(80);

// Variable to store the current effect
String currentEffect = "";

void setup() {
  Serial.begin(9600);
  delay(1000);

  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  FastLED.setBrightness(100); // Set initial brightness

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  // Print IP address
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Print hostname
  Serial.print("Hostname: ");
  Serial.println(WiFi.getHostname());

  // Print uptime
  Serial.print("Uptime: ");
  Serial.print(millis() / 1000);
  Serial.println(" seconds");

  // Start the server
  server.on("/setEffect", handleSetEffect);
  server.begin();
  Serial.println("Server started");
}

void handleSetEffect() {
  if (server.hasArg("effect")) {
    String effect = server.arg("effect");
    if (effect == "rainbow") {
      rainbow();
      server.send(200, "text/plain", "Rainbow effect started");
    } else if (effect == "colorwipe") {
      colorWipe(CRGB::Red, 1);
      server.send(200, "text/plain", "Color wipe effect started");
    } else if (effect == "theaterchase") {
      theaterChase(CRGB::Blue, 50);
      server.send(200, "text/plain", "Theater chase effect started");
    } else if (effect == "rainbowchase") {
      rainbowChase(20); // Change the delay time as needed
      server.send(200, "text/plain", "Rainbow chase effect started");
    } else if (effect == "whitestrobe") {
      whiteStrobe(5, 50, 100); // Adjust parameters as needed
      server.send(200, "text/plain", "White strobe effect started");
    } else if (effect == "clearlights") {
      clearLights();
      server.send(200, "text/plain", "Lights cleared");
    } else if (effect == "colorfade") {
      colorFade(CRGB::Red, CRGB::Blue, 100, 20); // Adjust parameters as needed
      server.send(200, "text/plain", "Color fade effect started");
    } else if (effect == "sparkle") {
      sparkle(CRGB::Yellow, 20); // Adjust parameters as needed
      server.send(200, "text/plain", "Sparkle effect started");
    } else if (effect == "meteorrain") {
      meteorRain(CRGB::Green, 10, 64, true); // Adjust parameters as needed
      server.send(200, "text/plain", "Meteor rain effect started");
    } else if (effect == "twinkle") {
      twinkle(CRGB::Cyan, 30, 100, true); // Adjust parameters as needed
      server.send(200, "text/plain", "Twinkle effect started");
    } else if (effect == "colorwipereverse") {
      colorWipeReverse(CRGB::Magenta, 10); // Adjust parameters as needed
      server.send(200, "text/plain", "Reverse color wipe effect started");
    } else if (effect == "theaterchaserainbow") {
      theaterChaseRainbow(50); // Change the delay time as needed
      server.send(200, "text/plain", "Rainbow theater chase effect started");
    } else if (effect == "confetti") {
      confetti(50); // Adjust parameters as needed
      server.send(200, "text/plain", "Confetti effect started");
    } else if (effect == "sinelon") {
      sinelon(CRGB::Orange, 30); // Adjust parameters as needed
      server.send(200, "text/plain", "Sinelon effect started");
    } else if (effect == "juggle") {
      juggle(5, 10); // Adjust parameters as needed
      server.send(200, "text/plain", "Juggle effect started");
    } else {
      server.send(400, "text/plain", "Invalid effect");
    }
  } else {
    server.send(400, "text/plain", "Missing 'effect' parameter");
  }
}

void loop() {
  server.handleClient(); // Handle incoming HTTP requests
}




void rainbow() {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = Wheel((i + millis() / 30) & 255);
  }
  FastLED.show();
  delay(20);
}

void colorWipe(CRGB color, int wait) {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = color;
    FastLED.show();
    delay(wait);
  }
}

void theaterChase(CRGB color, int wait) {
  for (int j = 0; j < 10; j++) { // Repeat 10 times
    for (int q = 0; q < 3; q++) {
      for (int i = 0; i < NUM_LEDS; i = i + 3) {
        leds[i + q] = color;
      }
      FastLED.show();
      delay(wait);
      for (int i = 0; i < NUM_LEDS; i = i + 3) {
        leds[i + q] = CRGB::Black;
      }
    }
  }
}
void rainbowChase(int wait) {
  for (int j = 0; j < 256; j++) { // Cycle all 256 colors in the wheel
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i] = Wheel(((i * 256 / NUM_LEDS) + j) & 255);
    }
    FastLED.show();
    delay(wait);
  }
}

void whiteStrobe(int count, int flashDuration, int wait) {
  for (int i = 0; i < count; i++) {
    fill_solid(leds, NUM_LEDS, CRGB::White);
    FastLED.show();
    delay(flashDuration);
    fill_solid(leds, NUM_LEDS, CRGB::Black);
    FastLED.show();
    delay(wait);
  }
}

void clearLights() {
  fill_solid(leds, NUM_LEDS, CRGB::Black);
  FastLED.show();
}

void colorFade(CRGB color1, CRGB color2, int steps, int wait) {
  for (int i = 0; i < steps; i++) {
    float ratio = float(i) / float(steps);
    CRGB color = blend(color1, color2, ratio);
    fill_solid(leds, NUM_LEDS, color);
    FastLED.show();
    delay(wait);
  }
}

void sparkle(CRGB color, int chanceOfSparkle) {
  for (int i = 0; i < NUM_LEDS; i++) {
    if (random(0, 100) < chanceOfSparkle) {
      leds[i] = color;
    }
  }
  FastLED.show();
}

void meteorRain(CRGB color, int meteorSize, int meteorTrailDecay, bool meteorRandomDecay) {
  fadeToBlackBy(leds, NUM_LEDS, meteorTrailDecay);
  for (int i = 0; i < NUM_LEDS; i++) {
    if (!meteorRandomDecay || random(10) > 5) {
      leds[i] = color;
    }
    FastLED.show();
    delay(meteorSize);
    if (!meteorRandomDecay) {
      fadeToBlackBy(leds, NUM_LEDS, meteorTrailDecay);
    }
  }
}

void twinkle(CRGB color, int count, int speed, bool onlyOne) {
  for (int i = 0; i < count; i++) {
    int pixel = random(NUM_LEDS);
    leds[pixel] = color;
    FastLED.show();
    if (onlyOne) {
      fill_solid(leds, NUM_LEDS, CRGB::Black);
    }
    delay(speed);
  }
}

void colorWipeReverse(CRGB color, int wait) {
  for (int i = NUM_LEDS - 1; i >= 0; i--) {
    leds[i] = color;
    FastLED.show();
    delay(wait);
  }
}

void theaterChaseRainbow(int wait) {
  for (int j = 0; j < 256; j++) { // Cycle all 256 colors in the wheel
    for (int q = 0; q < 3; q++) {
      for (int i = 0; i < NUM_LEDS; i = i + 3) {
        leds[i + q] = Wheel((i + j) % 255);
      }
      FastLED.show();
      delay(wait);
      for (int i = 0; i < NUM_LEDS; i = i + 3) {
        leds[i + q] = CRGB::Black;
      }
    }
  }
}

void confetti(int count) {
  for (int i = 0; i < count; i++) {
    int pos = random(NUM_LEDS);
    leds[pos] += CHSV(random(256), 200, 255);
    FastLED.show();
    delay(50);
  }
}

void sinelon(CRGB color, int speed) {
  int pos = beatsin16(speed, 0, NUM_LEDS - 1);
  fill_solid(leds, NUM_LEDS, CRGB::Black);
  leds[pos] = color;
  FastLED.show();
}

void juggle(int count, int fade) {
  fadeToBlackBy(leds, NUM_LEDS, fade);
  byte dothue = 0;
  for (int i = 0; i < count; i++) {
    leds[beatsin16(i + 7, 0, NUM_LEDS - 1)] |= CHSV(dothue, 200, 255);
    FastLED.show();
    delay(20);
    fadeToBlackBy(leds, NUM_LEDS, fade);
    dothue += 32;
  }
}


CRGB Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if (WheelPos < 85) {
    return CRGB(255 - WheelPos * 3, 0, WheelPos * 3);
  } else if (WheelPos < 170) {
    WheelPos -= 85;
    return CRGB(0, WheelPos * 3, 255 - WheelPos * 3);
  } else {
    WheelPos -= 170;
    return CRGB(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
}
