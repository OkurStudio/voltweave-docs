#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "VWVTypes.h"
#include "MyGridWatcher.generated.h"

/** Logs blackouts and recoveries of every network in the world. */
UCLASS()
class MYGAME_API AMyGridWatcher : public AActor
{
	GENERATED_BODY()

protected:
	virtual void BeginPlay() override;

	// Bound to the grid subsystem's On Network State Changed event.
	UFUNCTION()
	void HandleNetworkStateChanged(const FVWVNetworkInfo& Network, EVWVNetworkState PreviousState);

	void LogAllNetworks() const;
};
