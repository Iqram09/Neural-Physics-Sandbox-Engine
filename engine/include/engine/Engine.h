#pragma once

namespace engine {

class Engine {
public:
    Engine();
    ~Engine();

    // Initialize the engine
    bool Init();

    // Advance the engine by one tick/frame
    void Tick(float deltaTime);

    // Shutdown the engine and cleanup resources
    void Shutdown();

private:
    bool initialized_;
};

} // namespace engine