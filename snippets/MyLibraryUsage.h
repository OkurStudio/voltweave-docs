#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "MyLibraryUsage.generated.h"

/** Shows the Blueprint function library from C++. */
UCLASS()
class MYGAME_API AMyLibraryUsage : public AActor
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
