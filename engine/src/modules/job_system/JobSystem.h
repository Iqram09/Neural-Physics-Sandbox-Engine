#pragma once
#include <functional>
#include <vector>
#include <thread>

class JobSystem {
public:
    JobSystem();
    ~JobSystem();

    void Enqueue(std::function<void()> job);
    void WaitAll();
};
