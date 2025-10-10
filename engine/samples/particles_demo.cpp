#include "engine/Engine.h"
#include "modules/rendering/Renderer.h"
#include "modules/physics/PhysicsAdapter.h"
#include "modules/neural_sim/NeuralSimInterface.h"

int main() {
    Engine engine;
    engine.Init();
    // Choose physics or neural sim
    // Renderer renderer;
    // renderer.Init();
    // ...
    engine.Shutdown();
    return 0;
}
