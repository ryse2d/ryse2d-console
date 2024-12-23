#ifndef __HELLOWORLD_SCENE_H__
#define __HELLOWORLD_SCENE_H__

#include "ryse2d.h"

class HelloWorld : public ryse2d::Layer
{
public:
    // there's no 'id' in cpp, so we recommend returning the class instance pointer
    static ryse2d::Scene* createScene();

    // Here's a difference. Method 'init' in ryse2d-x returns bool, instead of returning 'id' in ryse2d-iphone
    virtual bool init();

    // implement the "static create()" method manually
    CREATE_FUNC(HelloWorld);
};

#endif // __HELLOWORLD_SCENE_H__
