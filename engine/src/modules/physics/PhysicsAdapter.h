#pragma once

class PhysicsAdapter {
public:
    virtual ~PhysicsAdapter() = default;
    virtual void Init() = 0;
    virtual void Step(float dt) = 0;
    virtual void Shutdown() = 0;
};
