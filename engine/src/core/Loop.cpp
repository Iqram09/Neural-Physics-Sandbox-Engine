#include <chrono>
#include <thread>
#include <functional>

class Loop {
public:
    Loop(double simTickRate, std::function<void()> simTick, std::function<void()> render)
        : simTickRate(simTickRate), simTick(simTick), render(render), running(false) {}

    void start() {
        using clock = std::chrono::high_resolution_clock;
        running = true;

        const double simTickDuration = 1.0 / simTickRate;
        double accumulator = 0.0;

        auto previous = clock::now();

        while (running) {
            auto current = clock::now();
            std::chrono::duration<double> elapsed = current - previous;
            previous = current;
            accumulator += elapsed.count();

            // Run simulation ticks as needed
            while (accumulator >= simTickDuration) {
                simTick();
                accumulator -= simTickDuration;
            }

            // Render (can interpolate using accumulator/simTickDuration if needed)
            render();

            // Optional: sleep to avoid busy waiting
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
        }
    }

    void stop() {
        running = false;
    }

private:
    double simTickRate;
    std::function<void()> simTick;
    std::function<void()> render;
    bool running;
};