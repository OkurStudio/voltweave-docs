#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "MyGridRewirer.generated.h"

class UVWVNodeComponent;

/** Keeps a generator wired to a lamp even when the lamp's node is recreated while playing. */
UCLASS()
class MYGAME_API AMyGridRewirer : public AActor
{
	GENERATED_BODY()

public:
	UPROPERTY(EditAnywhere, Category = "Grid")
	TObjectPtr<AActor> GeneratorActor;

	UPROPERTY(EditAnywhere, Category = "Grid")
	TObjectPtr<AActor> LampActor;

protected:
	virtual void BeginPlay() override;

	// Called whenever any node registers with the grid, including nodes that were just recreated.
	void HandleNodeRegistered(UVWVNodeComponent* Node);
};
