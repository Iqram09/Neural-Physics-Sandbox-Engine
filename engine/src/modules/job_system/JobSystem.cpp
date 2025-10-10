#include "JobSystem.h"

JobSystem::JobSystem() {}
JobSystem::~JobSystem() {}

void JobSystem::Enqueue(std::function<void()> job) {
    // Add job to queue
}

void JobSystem::WaitAll() {
    // Wait for all jobs to finish
}
