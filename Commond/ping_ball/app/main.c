#include <stdlib.h>
#include <raylib.h>

typedef struct {
    int array [2];
} Vec;

static const Vec normal_top = {{0, -1}};
static const Vec normal_bottom = {{0, 1}};
static const Vec normal_left = {{-1, 0}};
static const Vec normal_right = {{1, 0}};

/*
 * direction vector reflection based on given normal
 * v' = v - 2 * (v · n) * n
 */
static Vec reflect(Vec velocity, Vec normal) {
    int dot_product = (velocity.array[0] * normal.array[0]) + (velocity.array[1] * normal.array[1]);
    int r_vx = velocity.array[0] - 2 * dot_product * normal.array[0];
    int r_vy = velocity.array[1] - 2 * dot_product * normal.array[1];
    return (Vec) {.array = {r_vx, r_vy}};
}

/*
 * ball colors
 */
static const Color ball_colors[] = {
	{255, 0, 0, 255},     // Red
	{255, 127, 0, 255},   // Orange
	{255, 255, 0, 255},   // Yellow
	{0, 255, 0, 255},     // Green
	{0, 0, 255, 255},     // Blue
	{75, 0, 130, 255},    // Indigo
	{148, 0, 211, 255}    // Violet
};

#define BALL_RADIUS 20
#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 600

int main(void) {
    Color bg_color = {200, 200, 200, 255};
    Vec velocity = {.array = {1, 1}};
    int x = WINDOW_WIDTH / 2;
    int y = WINDOW_HEIGHT / 2;
	const int num_colors = sizeof(ball_colors) / sizeof(ball_colors[0]);
	int color_index = 0;

    /*
     * window setup
     */
    InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "Ping Ball");
    SetTargetFPS(25);

    /*
     * game loop
     */
    while(WindowShouldClose() == false) {
		/*
         * update of ball position
		 */
        x += velocity.array[0] * 4;
        y += velocity.array[1] * 4;

        /* 
         * change ball color
         */
		if(x <= BALL_RADIUS || x >= WINDOW_WIDTH - BALL_RADIUS 
				|| y <= BALL_RADIUS || y >= WINDOW_HEIGHT - BALL_RADIUS) {
			color_index = (color_index + 1) % num_colors;
		}

        /*
         * ball direction vector reflection
         */
        if(x <= BALL_RADIUS) {
            velocity = reflect(velocity, normal_left);
        } else if (x >= WINDOW_WIDTH - BALL_RADIUS) {
            velocity = reflect(velocity, normal_right);
        }

        if(y <= BALL_RADIUS) {
            velocity = reflect(velocity, normal_top);
        } else if (y >= WINDOW_HEIGHT - BALL_RADIUS) {
            velocity = reflect(velocity, normal_bottom);
        }

        /*
         * window content drawing
         */
        BeginDrawing();
        ClearBackground(bg_color);
        DrawCircle(x, y, BALL_RADIUS, ball_colors[color_index]);
        EndDrawing();
    }

    /*
     * clear environment
     */
    CloseWindow();

    return EXIT_SUCCESS;
}



