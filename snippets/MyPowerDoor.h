#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Components/VWVConsumerComponent.h"
#include "MyPowerDoor.generated.h"

class UStaticMeshComponent;

/** A door that is open only while it receives power. */
UCLASS()
class MYGAME_API AMyPowerDoor : public AActor
{
	GENERATED_BODY()

public:
	AMyPowerDoor();

protected:
	virtual void BeginPlay() override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Door")
	TObjectPtr<UStaticMeshComponent> Leaf;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Door")
	TObjectPtr<UVWVConsumerComponent> Power;

	// Bound to the consumer's On Power State Changed event. It runs on the server and on clients.
	UFUNCTION()
	void HandlePowerStateChanged(UVWVConsumerComponent* Consumer, EVWVConsumerState NewState, EVWVConsumerState OldState);

	void SetDoorOpen(bool bOpen);
};
