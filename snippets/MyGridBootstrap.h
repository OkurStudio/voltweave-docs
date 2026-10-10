#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "MyGridBootstrap.generated.h"

/** Adds a generator node and a lamp node to two existing Actors and wires them together when the game starts. */
UCLASS()
class MYGAME_API AMyGridBootstrap : public AActor
{
	GENERATED_BODY()

public:
	UPROPERTY(EditAnywhere, Category = "Grid")
	TObjectPtr<AActor> GeneratorActor;

	UPROPERTY(EditAnywhere, Category = "Grid")
	TObjectPtr<AActor> LampActor;

protected:
	virtual void BeginPlay() override;
};
