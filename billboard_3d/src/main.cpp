#include <raylib.h>

int main() {
  InitWindow(1600, 900, "game.out");
  SetTargetFPS(60);
  DisableCursor();

  Camera3D camera = {.position = {10, 0.5, 10},
                     .target = {5, 0.5, 5},
                     .up = {0, 1, 0},
                     .fovy = 60,
                     .projection = CAMERA_PERSPECTIVE};

  Texture2D wizard_texture = LoadTexture("./assets/wizard.png");

  while (!WindowShouldClose()) {
    UpdateCamera(&camera, CAMERA_FREE);

    BeginDrawing();
    ClearBackground(BLACK);

    BeginMode3D(camera);
    DrawPlane({10, 0, 10}, {20, 20}, GRAY);
    DrawGrid(20, 1);
    DrawBillboard(camera, wizard_texture, {5, 0.5, 5}, 1, WHITE);
    EndMode3D();

    DrawCircle(GetScreenWidth() / 2, GetScreenHeight() / 2, 4, RED);
    DrawFPS(10, 10);
    EndDrawing();
  }

  UnloadTexture(wizard_texture);

  CloseWindow();
}
