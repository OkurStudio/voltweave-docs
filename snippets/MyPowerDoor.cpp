#include "MyPowerDoor.h"

#include "Components/StaticMeshComponent.h"

AMyPowerDoor::AMyPowerDoor()
{
	// The Actor must replicate, otherwise clients never receive the state of its nodes.
	bReplicates = true;

	Leaf = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Leaf"));
	SetRootComponent(Leaf);

	Power = CreateDefaultSubobject<UVWVConsumerComponent>(TEXT("Power"));
	Power->SetupAttachment(Leaf);
	Power->RequestedWatts = 50.f;
}

void AMyPowerDoor::BeginPlay()
{
	Super::BeginPlay();

	Power->OnPowerStateChanged.AddDynamic(this, &AMyPowerDoor::HandlePowerStateChanged);
	SetDoorOpen(Power->IsPowered());
}

void AMyPowerDoor::HandlePowerStateChanged(UVWVConsumerComponent* Consumer, EVWVConsumerState NewState, EVWVConsumerState OldState)
{
	SetDoorOpen(NewState == EVWVConsumerState::Powered);
}

void AMyPowerDoor::SetDoorOpen(bool bOpen)
{
	Leaf->SetRelativeRotation(FRotator(0.f, bOpen ? 90.f : 0.f, 0.f));
}
