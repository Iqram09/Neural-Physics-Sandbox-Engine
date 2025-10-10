#pragma once

class NeuralSimInterface {
public:
    virtual ~NeuralSimInterface() = default;
    virtual void Init() = 0;
    virtual void Step(float dt) = 0;
    virtual void Shutdown() = 0;
};
